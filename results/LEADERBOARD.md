# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 8:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1393 windows, 35993 settled trades, 382 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 723 | 34.7 | 35.3 | $-483.87 | -6.7% | $516.13 | -1.4 | done | can't tell from luck |
| value_ev10 | 1747 | 38.9 | 39.2 | $-748.67 | -4.3% | $251.33 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3594 | 50.8 | 50.1 | $-1050.67 | -2.9% | $-50.67 | -1.7 | done | can't tell from luck |
| value_ev5 | 2632 | 40.6 | 41.1 | $-1243.36 | -4.7% | $-243.36 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3017 | 49.3 | 49.3 | $-1470.89 | -4.9% | $-470.89 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3017 | 50.7 | 50.9 | $-1568.41 | -5.2% | $-568.41 | -2.9 | done | losing for real |
| trend_filter | 2138 | 48.6 | 50.4 | $-1856.61 | -8.7% | $-856.61 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3594 | 49.2 | 50.2 | $-2209.77 | -6.1% | $-1209.77 | -3.7 | done | losing for real |
| coinflip | 5177 | 50.0 | 50.0 | $-2212.39 | -4.3% | $-1212.39 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5177 | 50.2 | 51.3 | $-3172.86 | -6.1% | $-2172.86 | -4.5 | done | losing for real |
| always_up | 5177 | 47.9 | 49.3 | $-3678.38 | -7.1% | $-2678.38 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9002 | 48.1 | 48.8 | $-4906.55 |
| ETH | 9681 | 48.1 | 48.0 | $-5205.11 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
