# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 10:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 115 windows, 2948 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 224 | 61.2 | 53.1 | $+292.83 | +13.1% | $1292.83 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 284 | 56.3 | 52.1 | $+172.44 | +6.1% | $1172.44 | +1.1 | done | can't tell from luck |
| momentum_5m_0.00pct | 453 | 52.3 | 50.7 | $-26.45 | -0.6% | $973.55 | -0.1 | done | can't tell from luck |
| value_ev10 | 151 | 40.4 | 40.7 | $-77.82 | -5.2% | $922.18 | -0.5 | Thu 8:30 AM | too few trades (151/200) |
| value_ev20 | 53 | 28.3 | 36.7 | $-131.54 | -24.8% | $868.46 | -1.5 | Sun 12:15 PM | too few trades (53/200) |
| coinflip | 453 | 50.6 | 51.3 | $-239.50 | -5.3% | $760.50 | -1.2 | done | can't tell from luck |
| value_ev5 | 214 | 38.8 | 42.1 | $-248.75 | -11.6% | $751.25 | -1.5 | done | can't tell from luck |
| trend_filter | 155 | 40.6 | 48.7 | $-297.88 | -19.2% | $702.12 | -2.4 | Thu 7:15 AM | too few trades (155/200) |
| momentum_15m_0.10pct | 284 | 43.7 | 50.1 | $-439.39 | -15.5% | $560.61 | -2.6 | done | losing for real |
| always_up | 453 | 46.8 | 50.5 | $-495.98 | -10.9% | $504.02 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 224 | 38.8 | 49.0 | $-509.37 | -22.7% | $490.63 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 637 | 46.2 | 49.8 | $-551.69 |
| ETH | 722 | 45.7 | 48.9 | $-684.94 |
| SOL | 785 | 48.2 | 48.6 | $-550.15 |
| XRP | 804 | 50.5 | 49.1 | $-214.63 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
