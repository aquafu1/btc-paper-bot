# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 5:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 279 windows, 7367 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 726 | 55.0 | 52.1 | $+114.01 | +1.6% | $1114.01 | +0.4 | done | can't tell from luck |
| value_ev20 | 136 | 36.0 | 36.9 | $-89.35 | -6.6% | $910.65 | -0.6 | Sun 4:30 AM | too few trades (136/200) |
| reversal_60m_0.30pct | 590 | 52.4 | 52.2 | $-199.08 | -3.4% | $800.92 | -0.9 | done | can't tell from luck |
| value_ev10 | 359 | 38.4 | 40.8 | $-333.02 | -9.3% | $666.98 | -1.5 | done | can't tell from luck |
| value_ev5 | 524 | 40.3 | 42.4 | $-466.88 | -8.9% | $533.12 | -1.8 | done | can't tell from luck |
| trend_filter | 392 | 46.4 | 50.3 | $-476.54 | -12.2% | $523.46 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 590 | 47.6 | 49.7 | $-520.58 | -8.8% | $479.42 | -2.2 | done | losing for real |
| coinflip | 1108 | 50.0 | 50.9 | $-651.00 | -5.9% | $349.00 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 1108 | 49.5 | 51.5 | $-879.07 | -7.9% | $120.93 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 726 | 45.0 | 49.8 | $-966.07 | -13.3% | $33.93 | -3.6 | done | losing for real |
| always_up | 1108 | 47.0 | 50.2 | $-1150.58 | -10.4% | $-150.58 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1647 | 46.8 | 49.5 | $-1582.76 |
| ETH | 1840 | 47.1 | 48.9 | $-1664.16 |
| SOL | 1908 | 48.2 | 49.4 | $-1454.01 |
| XRP | 1972 | 48.8 | 49.1 | $-917.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
