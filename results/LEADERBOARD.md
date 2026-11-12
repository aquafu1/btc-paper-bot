# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 10:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 116 windows, 2970 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 224 | 61.2 | 53.1 | $+292.83 | +13.1% | $1292.83 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 286 | 56.6 | 52.0 | $+204.19 | +7.1% | $1204.19 | +1.2 | done | can't tell from luck |
| momentum_5m_0.00pct | 457 | 52.1 | 50.8 | $-52.08 | -1.1% | $947.92 | -0.2 | done | can't tell from luck |
| value_ev10 | 153 | 40.5 | 40.6 | $-68.93 | -4.5% | $931.07 | -0.5 | Thu 8:15 AM | too few trades (153/200) |
| value_ev20 | 55 | 29.1 | 36.6 | $-122.65 | -22.3% | $877.35 | -1.3 | Sun 9:00 AM | too few trades (55/200) |
| value_ev5 | 216 | 38.9 | 42.1 | $-239.87 | -11.1% | $760.13 | -1.4 | done | can't tell from luck |
| coinflip | 457 | 50.3 | 51.3 | $-256.63 | -5.6% | $743.37 | -1.2 | done | can't tell from luck |
| trend_filter | 155 | 40.6 | 48.7 | $-297.88 | -19.2% | $702.12 | -2.4 | Thu 7:45 AM | too few trades (155/200) |
| momentum_15m_0.10pct | 286 | 43.4 | 50.1 | $-459.39 | -16.1% | $540.61 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 224 | 38.8 | 49.0 | $-509.37 | -22.7% | $490.63 | -3.4 | done | losing for real |
| always_up | 457 | 46.4 | 50.5 | $-535.98 | -11.7% | $464.02 | -2.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 643 | 45.9 | 49.7 | $-597.32 |
| ETH | 725 | 45.5 | 49.0 | $-714.94 |
| SOL | 790 | 48.1 | 48.6 | $-554.41 |
| XRP | 812 | 50.5 | 49.1 | $-179.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
