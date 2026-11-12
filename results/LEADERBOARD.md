# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 11:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 118 windows, 3016 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 224 | 61.2 | 53.1 | $+292.83 | +13.1% | $1292.83 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 288 | 56.2 | 51.8 | $+184.19 | +6.4% | $1184.19 | +1.1 | done | can't tell from luck |
| momentum_5m_0.00pct | 464 | 52.4 | 50.9 | $-50.62 | -1.1% | $949.38 | -0.2 | done | can't tell from luck |
| value_ev10 | 160 | 38.8 | 40.3 | $-138.93 | -8.7% | $861.07 | -0.9 | Thu 6:45 AM | too few trades (160/200) |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sat 10:45 PM | too few trades (61/200) |
| trend_filter | 156 | 41.0 | 48.8 | $-293.51 | -18.8% | $706.49 | -2.3 | Thu 7:45 AM | too few trades (156/200) |
| coinflip | 464 | 50.0 | 51.1 | $-297.88 | -6.4% | $702.12 | -1.4 | done | can't tell from luck |
| value_ev5 | 223 | 37.7 | 41.8 | $-309.87 | -13.9% | $690.13 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 288 | 43.8 | 50.3 | $-451.58 | -15.7% | $548.42 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 224 | 38.8 | 49.0 | $-509.37 | -22.7% | $490.63 | -3.4 | done | losing for real |
| always_up | 464 | 45.7 | 50.2 | $-605.98 | -13.1% | $394.02 | -2.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 649 | 45.6 | 49.6 | $-641.86 |
| ETH | 736 | 45.0 | 48.7 | $-811.14 |
| SOL | 805 | 48.0 | 48.5 | $-618.15 |
| XRP | 826 | 49.9 | 48.8 | $-292.22 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
