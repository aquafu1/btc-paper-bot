# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 7:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 104 windows, 2658 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 201 | 59.2 | 52.9 | $+183.80 | +9.1% | $1183.80 | +1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 255 | 55.7 | 52.1 | $+121.56 | +4.8% | $1121.56 | +0.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 408 | 52.7 | 50.7 | $+2.88 | +0.1% | $1002.88 | +0.0 | done | can't tell from luck |
| value_ev10 | 139 | 38.8 | 40.6 | $-119.31 | -8.6% | $880.69 | -0.9 | Thu 7:45 AM | too few trades (139/200) |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 7:15 AM | too few trades (50/200) |
| trend_filter | 143 | 42.7 | 49.0 | $-228.60 | -16.0% | $771.40 | -1.9 | Thu 6:30 AM | too few trades (143/200) |
| coinflip | 408 | 50.0 | 51.3 | $-261.61 | -6.4% | $738.39 | -1.3 | done | can't tell from luck |
| value_ev5 | 190 | 36.8 | 41.9 | $-293.38 | -15.4% | $706.62 | -1.9 | Wed 8:45 PM | too few trades (190/200) |
| momentum_15m_0.10pct | 255 | 44.3 | 50.0 | $-362.28 | -14.2% | $637.72 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 201 | 40.8 | 49.1 | $-391.39 | -19.5% | $608.61 | -2.8 | done | losing for real |
| always_up | 408 | 46.8 | 50.2 | $-425.37 | -10.4% | $574.63 | -2.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 571 | 45.7 | 49.6 | $-499.81 |
| ETH | 648 | 45.7 | 48.9 | $-596.64 |
| SOL | 710 | 48.2 | 48.5 | $-497.67 |
| XRP | 729 | 50.2 | 49.1 | $-303.44 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
