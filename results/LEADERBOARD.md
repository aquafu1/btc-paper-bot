# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 1:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 934 windows, 25842 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 476 | 35.1 | 34.8 | $-155.74 | -3.3% | $844.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1168 | 38.0 | 39.1 | $-683.12 | -5.8% | $316.88 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2205 | 50.2 | 49.8 | $-902.47 | -4.1% | $97.53 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2641 | 50.9 | 50.6 | $-936.61 | -3.5% | $63.39 | -1.8 | done | can't tell from luck |
| trend_filter | 1537 | 50.1 | 51.0 | $-1030.73 | -6.7% | $-30.73 | -2.7 | done | losing for real |
| value_ev5 | 1776 | 39.7 | 41.0 | $-1119.62 | -6.3% | $-119.62 | -2.2 | done | losing for real |
| coinflip | 3731 | 50.4 | 50.4 | $-1557.23 | -4.2% | $-557.23 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2205 | 49.8 | 50.9 | $-1576.60 | -7.2% | $-576.60 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 2641 | 49.1 | 50.3 | $-1651.55 | -6.3% | $-651.55 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3731 | 51.0 | 51.6 | $-1869.49 | -5.0% | $-869.49 | -3.2 | done | losing for real |
| always_up | 3731 | 46.7 | 49.7 | $-3881.61 | -10.4% | $-2881.61 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5885 | 48.1 | 49.1 | $-3473.24 |
| ETH | 6428 | 48.2 | 48.6 | $-4047.54 |
| SOL | 6744 | 48.2 | 48.6 | $-3971.56 |
| XRP | 6785 | 48.3 | 48.5 | $-3872.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
