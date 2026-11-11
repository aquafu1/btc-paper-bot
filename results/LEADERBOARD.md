# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 1:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 88 windows, 2225 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 344 | 56.1 | 50.8 | $+245.93 | +7.1% | $1245.93 | +1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 164 | 60.4 | 53.0 | $+187.15 | +11.4% | $1187.15 | +1.5 | Wed 5:30 PM | too few trades (164/200) |
| reversal_15m_0.10pct | 212 | 55.2 | 52.3 | $+75.60 | +3.6% | $1075.60 | +0.5 | done | can't tell from luck |
| value_ev10 | 116 | 42.2 | 40.1 | $-3.12 | -0.3% | $996.88 | -0.0 | Thu 4:30 AM | too few trades (116/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 7:15 PM | too few trades (43/200) |
| trend_filter | 123 | 46.3 | 48.6 | $-95.31 | -7.7% | $904.69 | -0.8 | Thu 2:15 AM | too few trades (123/200) |
| value_ev5 | 159 | 40.3 | 41.6 | $-118.55 | -7.5% | $881.45 | -0.8 | Wed 6:30 PM | too few trades (159/200) |
| coinflip | 344 | 49.7 | 51.6 | $-233.67 | -6.8% | $766.33 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 212 | 44.8 | 49.5 | $-259.52 | -12.2% | $740.48 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 164 | 39.6 | 48.7 | $-343.03 | -20.9% | $656.97 | -2.7 | Wed 5:30 PM | too few trades (164/200) |
| always_up | 344 | 46.5 | 50.2 | $-358.00 | -10.4% | $642.00 | -1.9 | done | can't tell from luck |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 478 | 48.3 | 49.8 | $-114.79 |
| ETH | 540 | 46.9 | 48.6 | $-291.53 |
| SOL | 595 | 49.7 | 48.5 | $-211.87 |
| XRP | 612 | 49.7 | 48.7 | $-338.18 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
