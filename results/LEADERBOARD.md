# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 5:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 143 windows, 3591 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 247 | 61.9 | 53.2 | $+342.92 | +13.9% | $1342.92 | +2.4 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 345 | 57.4 | 52.2 | $+247.75 | +7.2% | $1247.75 | +1.4 | done | can't tell from luck |
| momentum_5m_0.00pct | 564 | 52.3 | 51.3 | $-134.33 | -2.4% | $865.67 | -0.6 | done | can't tell from luck |
| value_ev20 | 70 | 30.0 | 36.9 | $-165.47 | -23.6% | $834.53 | -1.6 | Sun 3:15 AM | too few trades (70/200) |
| coinflip | 564 | 51.4 | 50.9 | $-218.34 | -3.9% | $781.66 | -1.0 | done | can't tell from luck |
| value_ev10 | 190 | 36.3 | 40.6 | $-285.28 | -15.0% | $714.72 | -1.8 | Thu 7:00 AM | too few trades (190/200) |
| trend_filter | 180 | 40.0 | 49.1 | $-388.37 | -21.6% | $611.63 | -2.9 | Thu 9:15 AM | too few trades (180/200) |
| value_ev5 | 275 | 37.5 | 42.2 | $-424.16 | -15.4% | $575.84 | -2.3 | done | losing for real |
| always_up | 564 | 47.0 | 50.0 | $-599.64 | -10.6% | $400.36 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 247 | 38.1 | 49.1 | $-615.20 | -24.9% | $384.80 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 345 | 42.6 | 50.0 | $-615.24 | -17.8% | $384.76 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 768 | 45.6 | 49.5 | $-839.59 |
| ETH | 887 | 45.0 | 48.7 | $-1064.44 |
| SOL | 948 | 48.4 | 48.8 | $-670.02 |
| XRP | 988 | 50.5 | 49.1 | $-281.31 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
