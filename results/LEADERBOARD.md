# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 10:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 116 windows, 2964 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 224 | 61.2 | 53.1 | $+292.83 | +13.1% | $1292.83 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 286 | 56.6 | 52.0 | $+204.19 | +7.1% | $1204.19 | +1.2 | done | can't tell from luck |
| momentum_5m_0.00pct | 456 | 52.0 | 50.7 | $-56.45 | -1.2% | $943.55 | -0.3 | done | can't tell from luck |
| value_ev10 | 152 | 40.8 | 40.7 | $-58.93 | -3.9% | $941.07 | -0.4 | Thu 8:15 AM | too few trades (152/200) |
| value_ev20 | 54 | 29.6 | 36.7 | $-112.65 | -20.9% | $887.35 | -1.2 | Sun 10:15 AM | too few trades (54/200) |
| value_ev5 | 215 | 39.1 | 42.1 | $-229.87 | -10.7% | $770.13 | -1.4 | done | can't tell from luck |
| coinflip | 456 | 50.4 | 51.3 | $-246.63 | -5.4% | $753.37 | -1.2 | done | can't tell from luck |
| trend_filter | 155 | 40.6 | 48.7 | $-297.88 | -19.2% | $702.12 | -2.4 | Thu 7:15 AM | too few trades (155/200) |
| momentum_15m_0.10pct | 286 | 43.4 | 50.1 | $-459.39 | -16.1% | $540.61 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 224 | 38.8 | 49.0 | $-509.37 | -22.7% | $490.63 | -3.4 | done | losing for real |
| always_up | 456 | 46.5 | 50.6 | $-525.98 | -11.5% | $474.02 | -2.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 637 | 46.2 | 49.8 | $-551.69 |
| ETH | 725 | 45.5 | 49.0 | $-714.94 |
| SOL | 790 | 48.1 | 48.6 | $-554.41 |
| XRP | 812 | 50.5 | 49.1 | $-179.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
