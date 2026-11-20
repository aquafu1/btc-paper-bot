# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 4:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 944 windows, 26158 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 483 | 35.0 | 34.9 | $-173.29 | -3.6% | $826.71 | -0.6 | done | can't tell from luck |
| value_ev10 | 1186 | 38.0 | 39.1 | $-691.30 | -5.8% | $308.70 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2674 | 51.0 | 50.6 | $-900.16 | -3.4% | $99.84 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2236 | 50.0 | 49.8 | $-975.88 | -4.4% | $24.12 | -2.1 | done | losing for real |
| trend_filter | 1555 | 49.9 | 51.0 | $-1093.30 | -7.0% | $-93.30 | -2.9 | done | losing for real |
| value_ev5 | 1801 | 39.8 | 41.0 | $-1113.35 | -6.2% | $-113.35 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 2236 | 50.0 | 50.9 | $-1555.18 | -7.0% | $-555.18 | -3.4 | done | losing for real |
| coinflip | 3771 | 50.4 | 50.4 | $-1593.97 | -4.2% | $-593.97 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2674 | 49.0 | 50.2 | $-1744.71 | -6.5% | $-744.71 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3771 | 50.9 | 51.6 | $-1936.51 | -5.1% | $-936.51 | -3.3 | done | losing for real |
| always_up | 3771 | 46.8 | 49.7 | $-3839.16 | -10.2% | $-2839.16 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5966 | 48.2 | 49.0 | $-3446.93 |
| ETH | 6499 | 48.1 | 48.6 | $-4116.13 |
| SOL | 6823 | 48.2 | 48.6 | $-3945.59 |
| XRP | 6870 | 48.3 | 48.5 | $-4108.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
