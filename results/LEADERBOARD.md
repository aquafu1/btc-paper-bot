# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 12:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 307 windows, 8202 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 667 | 52.9 | 51.7 | $-135.29 | -2.0% | $864.71 | -0.5 | done | can't tell from luck |
| value_ev20 | 152 | 34.9 | 36.5 | $-150.14 | -9.9% | $849.86 | -1.0 | Sun 2:15 AM | too few trades (152/200) |
| reversal_15m_0.10pct | 812 | 53.1 | 51.8 | $-159.84 | -2.0% | $840.16 | -0.6 | done | can't tell from luck |
| value_ev10 | 395 | 38.2 | 40.5 | $-386.52 | -9.8% | $613.48 | -1.7 | done | can't tell from luck |
| value_ev5 | 584 | 39.7 | 42.2 | $-592.64 | -10.1% | $407.36 | -2.2 | done | losing for real |
| trend_filter | 453 | 45.5 | 50.4 | $-642.16 | -14.2% | $357.84 | -3.1 | done | losing for real |
| momentum_60m_0.30pct | 667 | 47.1 | 50.0 | $-705.35 | -10.6% | $294.65 | -2.8 | done | losing for real |
| coinflip | 1220 | 49.9 | 50.9 | $-754.14 | -6.2% | $245.86 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 812 | 46.9 | 49.9 | $-829.91 | -10.2% | $170.09 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1220 | 48.7 | 51.3 | $-1128.61 | -9.3% | $-128.61 | -3.4 | done | losing for real |
| always_up | 1220 | 47.5 | 50.4 | $-1217.79 | -10.0% | $-217.79 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1844 | 46.5 | 49.3 | $-1811.87 |
| ETH | 2050 | 47.1 | 48.8 | $-1903.17 |
| SOL | 2131 | 48.1 | 49.4 | $-1714.51 |
| XRP | 2177 | 48.6 | 49.1 | $-1272.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
