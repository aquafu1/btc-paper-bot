# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 8:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1394 windows, 36002 settled trades, 394 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 723 | 34.7 | 35.3 | $-483.87 | -6.7% | $516.13 | -1.4 | done | can't tell from luck |
| value_ev10 | 1747 | 38.9 | 39.2 | $-748.67 | -4.3% | $251.33 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3595 | 50.8 | 50.1 | $-1039.05 | -2.9% | $-39.05 | -1.7 | done | can't tell from luck |
| value_ev5 | 2633 | 40.6 | 41.1 | $-1231.74 | -4.7% | $-231.74 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 3018 | 49.3 | 49.3 | $-1480.89 | -4.9% | $-480.89 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3018 | 50.7 | 50.9 | $-1556.79 | -5.2% | $-556.79 | -2.9 | done | losing for real |
| trend_filter | 2139 | 48.6 | 50.4 | $-1866.61 | -8.7% | $-866.61 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3595 | 49.2 | 50.2 | $-2219.77 | -6.2% | $-1219.77 | -3.7 | done | losing for real |
| coinflip | 5178 | 50.0 | 50.0 | $-2222.39 | -4.3% | $-1222.39 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5178 | 50.2 | 51.3 | $-3182.86 | -6.1% | $-2182.86 | -4.6 | done | losing for real |
| always_up | 5178 | 47.9 | 49.3 | $-3666.76 | -7.1% | $-2666.76 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9002 | 48.1 | 48.8 | $-4906.55 |
| ETH | 9690 | 48.1 | 48.0 | $-5208.62 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
