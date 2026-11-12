# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 7:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 105 windows, 2678 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 201 | 59.2 | 52.9 | $+183.80 | +9.1% | $1183.80 | +1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 259 | 54.8 | 52.0 | $+81.56 | +3.1% | $1081.56 | +0.5 | done | can't tell from luck |
| momentum_5m_0.00pct | 412 | 52.7 | 50.7 | $-3.35 | -0.1% | $996.65 | -0.0 | done | can't tell from luck |
| value_ev10 | 139 | 38.8 | 40.6 | $-119.31 | -8.6% | $880.69 | -0.9 | Thu 8:00 AM | too few trades (139/200) |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 8:15 AM | too few trades (50/200) |
| trend_filter | 143 | 42.7 | 49.0 | $-228.60 | -16.0% | $771.40 | -1.9 | Thu 7:00 AM | too few trades (143/200) |
| coinflip | 412 | 50.0 | 51.3 | $-267.84 | -6.5% | $732.16 | -1.4 | done | can't tell from luck |
| value_ev5 | 190 | 36.8 | 41.9 | $-293.38 | -15.4% | $706.62 | -1.9 | Wed 9:00 PM | too few trades (190/200) |
| momentum_15m_0.10pct | 259 | 45.2 | 50.1 | $-335.70 | -13.0% | $664.30 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 201 | 40.8 | 49.1 | $-391.39 | -19.5% | $608.61 | -2.8 | done | losing for real |
| always_up | 412 | 46.4 | 50.2 | $-465.37 | -11.3% | $534.63 | -2.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 576 | 45.5 | 49.6 | $-533.07 |
| ETH | 653 | 45.5 | 48.8 | $-630.56 |
| SOL | 715 | 48.3 | 48.5 | $-495.75 |
| XRP | 734 | 50.3 | 49.1 | $-304.05 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
