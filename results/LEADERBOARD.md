# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 7:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 105 windows, 2686 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 202 | 59.4 | 53.0 | $+191.11 | +9.5% | $1191.11 | +1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 260 | 55.0 | 52.0 | $+88.87 | +3.4% | $1088.87 | +0.6 | done | can't tell from luck |
| momentum_5m_0.00pct | 413 | 52.5 | 50.7 | $-13.35 | -0.3% | $986.65 | -0.1 | done | can't tell from luck |
| value_ev10 | 139 | 38.8 | 40.6 | $-119.31 | -8.6% | $880.69 | -0.9 | Thu 8:30 AM | too few trades (139/200) |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 9:15 AM | too few trades (50/200) |
| trend_filter | 144 | 42.4 | 49.0 | $-238.60 | -16.6% | $761.40 | -2.0 | Thu 7:00 AM | too few trades (144/200) |
| coinflip | 413 | 49.9 | 51.3 | $-277.84 | -6.7% | $722.16 | -1.4 | done | can't tell from luck |
| value_ev5 | 190 | 36.8 | 41.9 | $-293.38 | -15.4% | $706.62 | -1.9 | Wed 9:15 PM | too few trades (190/200) |
| momentum_15m_0.10pct | 260 | 45.0 | 50.1 | $-345.70 | -13.3% | $654.30 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 202 | 40.6 | 49.1 | $-401.39 | -19.9% | $598.61 | -2.8 | done | losing for real |
| always_up | 413 | 46.5 | 50.2 | $-458.06 | -11.1% | $541.94 | -2.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 584 | 45.4 | 49.6 | $-561.15 |
| ETH | 653 | 45.5 | 48.8 | $-630.56 |
| SOL | 715 | 48.3 | 48.5 | $-495.75 |
| XRP | 734 | 50.3 | 49.1 | $-304.05 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
