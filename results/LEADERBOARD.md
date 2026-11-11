# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 12:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 84 windows, 2121 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 328 | 56.7 | 50.9 | $+273.85 | +8.3% | $1273.85 | +1.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 154 | 58.4 | 52.8 | $+129.22 | +8.4% | $1129.22 | +1.1 | Wed 6:00 PM | too few trades (154/200) |
| reversal_15m_0.10pct | 202 | 55.9 | 52.1 | $+109.14 | +5.4% | $1109.14 | +0.8 | done | can't tell from luck |
| value_ev10 | 114 | 43.0 | 40.1 | $+16.88 | +1.5% | $1016.88 | +0.1 | Thu 3:15 AM | too few trades (114/200) |
| trend_filter | 114 | 48.2 | 48.7 | $-43.05 | -3.8% | $956.95 | -0.4 | Thu 3:15 AM | too few trades (114/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 2:45 PM | too few trades (43/200) |
| value_ev5 | 154 | 41.6 | 41.5 | $-68.55 | -4.5% | $931.45 | -0.5 | Wed 6:00 PM | too few trades (154/200) |
| coinflip | 328 | 50.3 | 51.5 | $-180.09 | -5.5% | $819.91 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 154 | 41.6 | 48.7 | $-263.47 | -17.1% | $736.53 | -2.1 | Wed 6:00 PM | too few trades (154/200) |
| momentum_15m_0.10pct | 202 | 44.1 | 49.5 | $-275.26 | -13.6% | $724.74 | -1.9 | done | can't tell from luck |
| always_up | 328 | 47.3 | 50.1 | $-284.24 | -8.7% | $715.76 | -1.6 | done | can't tell from luck |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 456 | 48.5 | 49.8 | $-74.10 |
| ETH | 514 | 47.7 | 48.6 | $-174.97 |
| SOL | 567 | 50.4 | 48.4 | $-114.95 |
| XRP | 584 | 50.0 | 48.5 | $-275.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
