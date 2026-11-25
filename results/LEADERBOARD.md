# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 8:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1392 windows, 35976 settled trades, 389 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 723 | 34.7 | 35.3 | $-483.87 | -6.7% | $516.13 | -1.4 | done | can't tell from luck |
| value_ev10 | 1747 | 38.9 | 39.2 | $-748.67 | -4.3% | $251.33 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3592 | 50.8 | 50.1 | $-1052.76 | -2.9% | $-52.76 | -1.8 | done | can't tell from luck |
| value_ev5 | 2631 | 40.6 | 41.1 | $-1250.24 | -4.8% | $-250.24 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3015 | 49.3 | 49.3 | $-1467.77 | -4.9% | $-467.77 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3015 | 50.7 | 51.0 | $-1570.50 | -5.2% | $-570.50 | -2.9 | done | losing for real |
| trend_filter | 2136 | 48.6 | 50.3 | $-1853.49 | -8.7% | $-853.49 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3592 | 49.2 | 50.2 | $-2206.65 | -6.1% | $-1206.65 | -3.7 | done | losing for real |
| coinflip | 5175 | 50.0 | 50.0 | $-2214.48 | -4.3% | $-1214.48 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5175 | 50.2 | 51.3 | $-3169.74 | -6.1% | $-2169.74 | -4.5 | done | losing for real |
| always_up | 5175 | 47.9 | 49.3 | $-3680.48 | -7.1% | $-2680.48 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8994 | 48.1 | 48.8 | $-4914.91 |
| ETH | 9672 | 48.1 | 48.0 | $-5199.51 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
