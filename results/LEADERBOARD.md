# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 10:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 76 windows, 1887 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 296 | 56.4 | 50.8 | $+224.77 | +7.6% | $1224.77 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 132 | 61.4 | 52.7 | $+187.51 | +14.2% | $1187.51 | +1.7 | Wed 7:30 PM | too few trades (132/200) |
| reversal_15m_0.10pct | 176 | 57.4 | 52.0 | $+142.16 | +8.1% | $1142.16 | +1.1 | Wed 12:30 PM | too few trades (176/200) |
| value_ev10 | 101 | 42.6 | 39.5 | $+9.52 | +0.9% | $1009.52 | +0.1 | Thu 4:00 AM | too few trades (101/200) |
| value_ev20 | 42 | 33.3 | 35.7 | $-43.85 | -10.4% | $956.15 | -0.5 | Sat 7:30 AM | too few trades (42/200) |
| value_ev5 | 140 | 40.7 | 41.1 | $-88.07 | -6.3% | $911.93 | -0.6 | Wed 5:45 PM | too few trades (140/200) |
| trend_filter | 100 | 45.0 | 48.5 | $-103.85 | -10.4% | $896.15 | -1.0 | Thu 4:15 AM | too few trades (100/200) |
| coinflip | 296 | 50.0 | 51.6 | $-189.98 | -6.4% | $810.02 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 176 | 42.6 | 49.3 | $-287.58 | -16.3% | $712.42 | -2.2 | Wed 12:30 PM | too few trades (176/200) |
| momentum_60m_0.30pct | 132 | 38.6 | 48.4 | $-292.36 | -22.1% | $707.64 | -2.5 | Wed 7:30 PM | too few trades (132/200) |
| always_up | 296 | 44.6 | 50.2 | $-421.94 | -14.3% | $578.06 | -2.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 397 | 47.1 | 49.7 | $-155.21 |
| ETH | 452 | 46.5 | 48.5 | $-277.23 |
| SOL | 512 | 49.2 | 48.1 | $-247.09 |
| XRP | 526 | 50.4 | 48.3 | $-184.14 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
