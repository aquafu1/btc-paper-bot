# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 9:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 246 windows, 6437 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 634 | 56.0 | 52.2 | $+207.29 | +3.3% | $1207.29 | +0.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 509 | 54.0 | 52.2 | $-15.99 | -0.3% | $984.01 | -0.1 | done | can't tell from luck |
| value_ev20 | 114 | 34.2 | 36.7 | $-120.27 | -10.6% | $879.73 | -0.9 | Sun 11:30 AM | too few trades (114/200) |
| value_ev10 | 310 | 37.1 | 40.9 | $-393.26 | -12.7% | $606.74 | -1.9 | done | can't tell from luck |
| trend_filter | 339 | 45.4 | 50.4 | $-470.18 | -13.9% | $529.82 | -2.6 | done | losing for real |
| value_ev5 | 457 | 39.4 | 42.6 | $-525.11 | -11.5% | $474.89 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 509 | 46.0 | 49.9 | $-623.35 | -12.2% | $376.65 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 977 | 49.9 | 51.6 | $-707.55 | -7.2% | $292.45 | -2.4 | done | losing for real |
| coinflip | 977 | 49.2 | 50.9 | $-747.79 | -7.7% | $252.21 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 634 | 44.0 | 49.9 | $-985.39 | -15.5% | $14.61 | -4.0 | done | losing for real |
| always_up | 977 | 47.1 | 50.5 | $-1083.69 | -11.1% | $-83.69 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1438 | 46.4 | 49.8 | $-1523.71 |
| ETH | 1603 | 46.6 | 49.1 | $-1670.98 |
| SOL | 1672 | 48.2 | 49.4 | $-1340.24 |
| XRP | 1724 | 48.7 | 49.2 | $-930.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
