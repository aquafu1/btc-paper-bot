# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 10:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 115 windows, 2945 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 224 | 61.2 | 53.1 | $+292.83 | +13.1% | $1292.83 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 284 | 56.3 | 52.1 | $+172.44 | +6.1% | $1172.44 | +1.1 | done | can't tell from luck |
| momentum_5m_0.00pct | 452 | 52.2 | 50.7 | $-33.47 | -0.7% | $966.53 | -0.2 | done | can't tell from luck |
| value_ev10 | 151 | 40.4 | 40.7 | $-77.82 | -5.2% | $922.18 | -0.5 | Thu 8:00 AM | too few trades (151/200) |
| value_ev20 | 53 | 28.3 | 36.7 | $-131.54 | -24.8% | $868.46 | -1.5 | Sun 11:30 AM | too few trades (53/200) |
| coinflip | 452 | 50.7 | 51.3 | $-229.50 | -5.1% | $770.50 | -1.1 | done | can't tell from luck |
| value_ev5 | 214 | 38.8 | 42.1 | $-248.75 | -11.6% | $751.25 | -1.5 | done | can't tell from luck |
| trend_filter | 155 | 40.6 | 48.7 | $-297.88 | -19.2% | $702.12 | -2.4 | Thu 7:00 AM | too few trades (155/200) |
| momentum_15m_0.10pct | 284 | 43.7 | 50.1 | $-439.39 | -15.5% | $560.61 | -2.6 | done | losing for real |
| always_up | 452 | 46.7 | 50.5 | $-502.99 | -11.1% | $497.01 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 224 | 38.8 | 49.0 | $-509.37 | -22.7% | $490.63 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 634 | 46.1 | 49.8 | $-555.73 |
| ETH | 722 | 45.7 | 48.9 | $-684.94 |
| SOL | 785 | 48.2 | 48.6 | $-550.15 |
| XRP | 804 | 50.5 | 49.1 | $-214.63 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
