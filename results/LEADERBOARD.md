# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 9:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 247 windows, 6458 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 637 | 55.7 | 52.2 | $+177.29 | +2.8% | $1177.29 | +0.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 511 | 53.8 | 52.2 | $-35.99 | -0.7% | $964.01 | -0.2 | done | can't tell from luck |
| value_ev20 | 114 | 34.2 | 36.7 | $-120.27 | -10.6% | $879.73 | -0.9 | Sun 11:30 AM | too few trades (114/200) |
| value_ev10 | 310 | 37.1 | 40.9 | $-393.26 | -12.7% | $606.74 | -1.9 | done | can't tell from luck |
| trend_filter | 341 | 45.7 | 50.4 | $-454.33 | -13.3% | $545.67 | -2.5 | done | losing for real |
| value_ev5 | 457 | 39.4 | 42.6 | $-525.11 | -11.5% | $474.89 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 511 | 46.2 | 50.0 | $-607.51 | -11.9% | $392.49 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 980 | 50.1 | 51.6 | $-683.78 | -7.0% | $316.22 | -2.3 | done | losing for real |
| coinflip | 980 | 49.4 | 50.9 | $-724.03 | -7.4% | $275.97 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 637 | 44.3 | 49.9 | $-961.62 | -15.1% | $38.38 | -3.9 | done | losing for real |
| always_up | 980 | 46.9 | 50.5 | $-1113.69 | -11.4% | $-113.69 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1446 | 46.5 | 49.8 | $-1514.10 |
| ETH | 1611 | 46.7 | 49.1 | $-1661.37 |
| SOL | 1672 | 48.2 | 49.4 | $-1340.24 |
| XRP | 1729 | 48.8 | 49.2 | $-926.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
